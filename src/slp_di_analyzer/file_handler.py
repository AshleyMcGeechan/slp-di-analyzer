import os, re, sys
import numpy as np
from peppi_py import read_slippi, read_peppi


def filter_file(filedata):
    arr = np.reshape(filedata, shape=(-1, 2, 9))
    
    # SPECIAL CASE: throws do not apply hitstun so our normal filtering method wouldn't work
    # This code finds the transition between thrown state to damaged state (when DI for throws is calculated) and sets hitstun to 1 and last attack landed to the corresponding throw
    
    # Find all instances of being in thrown state
    throw_mask_0_0 = np.logical_and(arr[:, 0, 4].astype(np.float32) >= 239, arr[:, 0, 4].astype(np.float32) <= 243)
    throw_mask_0_1 = np.logical_and(arr[:, 1, 4].astype(np.float32) >= 239, arr[:, 1, 4].astype(np.float32) <= 243)
    throw_mask_0 = np.logical_or(throw_mask_0_0, throw_mask_0_1)

    # Same values offset by one frame
    arr2 = np.array(arr, copy=True)
    arr2 = np.roll(arr2, -1, axis=0)
    throw_mask_1 = np.roll(throw_mask_0, -1, axis=0)
    
    # If in thrown state one frame and damaged state next frame set hitstun to 1 and lastattacklanded to throw
    transition_mask = np.logical_and(throw_mask_0, np.logical_not(throw_mask_1))
    arr[transition_mask, :, 8] = '1.0'
    arr[transition_mask, :, 7] = arr2[transition_mask, :, 7]

    # All frames where a player is in the last frame of hitstun
    mask1 = (arr[:, 0, 8] == '1.0')
    mask2 = (arr[:, 1, 8] == '1.0')
    mask = np.logical_or(mask1, mask2)
    arr = arr[mask, :, :]
    # Covers cases where both characters are in a damaged state
    arr = np.unique(arr, axis=0)
    return arr

def load_files(file):

    arr = []
    try:
        # This function prints "None" which is kind of ugly but I couldn't find a great way to prevent it
        # Suppressing stdout makes the function fail sometimes and clearing lines is awkward due to multithreading
        # ¯\_(ツ)_/¯
        game = read_slippi(str(file)) 

        # Check file is netplay game and not console mirror
        if (game.metadata["playedOn"] == 'dolphin'):
            
            # Joystick x and y are stick coordinates
            # Character is for filtering by character
            # State is internal action state, needed to determine which character was hit
            # Direction is character facing direction, needed to determine which side character was hit from as characters face the direction they were hit
            # Percent is for filtering by percent
            # Last attack landed is for filtering by move
            # Hitlag is the frames remaining of hitlag, stick coordinates for DI are read on last frame of hitlag
            
            player1 = game.frames.ports[0].leader
            player1_array = [player1.pre.joystick.x.to_numpy(), 
                                player1.pre.joystick.y.to_numpy(),
                                player1.post.character.to_numpy(), 
                                player1.post.state.to_numpy(), 
                                player1.post.direction.to_numpy(), 
                                player1.post.percent.to_numpy(), 
                                player1.post.last_attack_landed.to_numpy(), 
                                player1.post.hitlag.to_numpy()]
            player1_numpy = np.stack(player1_array, axis=-1)

            
            player2 = game.frames.ports[1].leader
            player2_array = [player2.pre.joystick.x.to_numpy(), 
                                player2.pre.joystick.y.to_numpy(), 
                                player2.post.character.to_numpy(), 
                                player2.post.state.to_numpy(), 
                                player2.post.direction.to_numpy(), 
                                player2.post.percent.to_numpy(), 
                                player2.post.last_attack_landed.to_numpy(), 
                                player2.post.hitlag.to_numpy()]
            player2_numpy = np.stack(player2_array, axis=-1)

            
            arr = np.stack((player1_numpy, player2_numpy), axis=1)
            arr = arr.reshape((-1,2,8))
            
            # Extracting connect code and appending it to frame data for filtering
            connect1 = re.sub(r'\W+', '', game.start.players[0].netplay.code).lower()
            connect2 = re.sub(r'\W+', '', game.start.players[1].netplay.code).lower()
            pad = np.tile([connect1, connect2], arr.shape[0]).reshape((-1,2,1))
            arr = np.concatenate((pad, arr), axis = 2)
            arr = filter_file(arr)
            arr = arr.flatten().tolist()
    except:
        print("Unable to load Slippi file: " + str(file))
    return arr