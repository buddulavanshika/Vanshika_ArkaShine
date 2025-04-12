import numpy as np

def interpolation(data):
   
    new_index = np.linspace(0, len(data) - 1, 1000)

    # Step 3: Reindex and interpolate
    reindexed_data = data.reindex(new_index)
    interpolated_data = reindexed_data.interpolate(method='linear')

    # Step 4: Add random noise to the interpolated data
    noise_scale = 0.05  # Adjust this for desired variation
    noisy_interpolated_data = interpolated_data + np.random.normal(0, noise_scale, interpolated_data.shape)

    # Optionally reset the index if needed
    noisy_interpolated_data.reset_index(drop=True, inplace=True)
    return noisy_interpolated_data
new_data=interpolation(df_filled_soil)
new_target=interpolation(df_filled_soil_target)
new_data.to_csv("new_data.csv",index=False)
new_target.to_csv("new_target.csv",index=False)
   

# Now noisy_interpolated_data has the original values with interpolation and noise
print("new dataset is created")
