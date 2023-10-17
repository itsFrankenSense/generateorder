import os
import random
import json

def get_num_nfts():
    while True:
        try:
            num_nfts = int(input("Enter the number of NFTs to generate: "))
            if num_nfts <= 0:
                print("Please enter a positive number.")
            else:
                return num_nfts
        except ValueError:
            print("Invalid input. Please enter a valid number.")

root_directory = 'Content'  # Replace with your project's root directory name (if different to 'Content')

# Read the traits from the directory structure
trait_types = sorted(os.listdir(root_directory), key=lambda x: (int(x.split('.')[0]), x.split('.')[1]))  # This sorts by the priority number

traits_dict = {}
all_traits_with_inscriptions = {}
usage_stats = {}

for trait_type in trait_types:
    trait_type_name = trait_type.split('. ')[1]  # Assuming the format is "1. Background"
    traits = os.listdir(os.path.join(root_directory, trait_type))

    traits_dict[trait_type_name] = traits

    # Initialize usage statistics
    usage_stats[trait_type_name] = {trait.split('.')[0]: 0 for trait in traits}

    # Ask for inscription IDs for each trait and store them
    print(f"\nPlease enter the Inscription IDs for the trait type: {trait_type_name}")
    trait_with_inscription = {}
    for trait in traits:
        trait_name = trait.split('.')[0]  # Assuming the trait files might have extensions and you need the name only
        inscription_id = input(f"Inscription ID for {trait_name}: ")
        trait_with_inscription[trait_name] = inscription_id

    all_traits_with_inscriptions[trait_type_name] = trait_with_inscription

    # Add a newline here for cleaner output
    print()

def create_random_nft(usage_stats):
    nft_traits = []
    for trait_type, traits in traits_dict.items():
        trait_value = random.choice(traits)
        trait_name = trait_value.split('.')[0]  # Assuming the trait files might have extensions and you need the name only

        # Update usage statistics
        usage_stats[trait_type][trait_name] += 1

        nft_traits.append({
            "trait_type": trait_type,
            "value": trait_name
        })
    return nft_traits

# Generate the NFTs based on user input
num_nfts = get_num_nfts()
nft_collection = [create_random_nft(usage_stats) for _ in range(num_nfts)]

# Save NFT metadata to a JSON file
with open('metadata.json', 'w') as outfile:
    json.dump(nft_collection, outfile, indent=4)

# Save all traits with their inscription IDs to a JSON file
with open('traits.json', 'w') as outfile:
    json.dump(all_traits_with_inscriptions, outfile, indent=4)

# Calculate trait usage statistics
trait_usage_percentages = {}
for trait_type, trait_counts in usage_stats.items():
    trait_usage_percentages[trait_type] = {}
    for trait_name, count in trait_counts.items():
        percentage = (count / num_nfts) * 100
        trait_usage_percentages[trait_type][trait_name] = f"{percentage:.2f}%"

# Save trait usage statistics to a JSON file
with open('trait_usage_statistics.json', 'w') as outfile:
    json.dump(trait_usage_percentages, outfile, indent=4)

print(f"\nGenerated metadata for {num_nfts} NFTs.")
print("The metadata has been saved to 'metadata.json'.")
print("The traits with their inscription IDs have been saved to 'traits.json'.")
print("Trait usage statistics have been saved to 'trait_usage_statistics.json'.")
