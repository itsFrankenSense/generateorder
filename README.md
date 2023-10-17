# Generatorder

## This code is to be used in conjunction with https://www.generatord.io/.

This repository contains the code and documentation for generating a collection of digital artifacts. Each unique piece of art is based on a combination of digital assets that are randomly assembled to create a unique digital collectible.

Please see the Youtube video for more details - TO BE RELEASED

## Features

- Random generation of unique NFT traits.
- Ability to assign inscription IDs to specific traits.
- Generation of metadata for each NFT.
- Calculation of trait usage statistics across the NFT collection.
- Export of NFT metadata and traits information to JSON files.

## Folder Structure
- Make sure the randomcollection.py is in the same folder as your 'Content' folder.
- The structure should be Main Folder (including code) > Content > Numbered Trait Type Folders > Trait Name files

### THIS IS 99% chatGPT code BEWARE

## Caveats

While this project serves as a robust starting point for generating NFT-based digital artwork, users should be aware of several nuances and limitations inherent in the current design:

1. **Randomness and Uniqueness:** The script generates traits for NFTs randomly. As such, there is no guarantee of creating a completely unique set of NFTs every time the script runs, especially with a large number of NFTs. Users should implement additional checks if uniqueness is a critical requirement.

2. **Performance:** Generating a very high number of NFTs could impact performance based on the system's capabilities. This script is not optimized for generating an extremely large number of NFTs in its current state.

3. **Security:** The script prompts users for Inscription IDs for traits, and no validation is done on the input. There's a risk of script injection if the inputs are not properly sanitized and validated, especially if used in a different environment.

4. **Dependency on File Structure:** The script's ability to correctly read and interpret traits depends heavily on the specific file and directory structure. Any deviation from the expected structure could result in errors or unexpected behavior.

5. **No Error Handling for File Operations:** The script performs file I/O operations (like reading directories and writing files), but it doesn't robustly handle potential file-related errors (e.g., lack of permissions, disk space exhaustion, or issues with file paths).
