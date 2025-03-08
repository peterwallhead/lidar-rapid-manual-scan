import os
import time
from datetime import datetime

import keyboard

from lidar import LidarStreamer
from scene import Frame


def format_scan_data(scan):
    formatted_scan_data = []
    for (key, value) in scan.items():
        formatted_scan_data.append((int(float(key)), value))
    return sorted(formatted_scan_data)

def main():
	lidar_stream = LidarStreamer()
	lidar_stream.start()  # Start continuous scanning
	time.sleep(2)

	# Create directories and data file for scan collection
	collection_dir_name = datetime.now().strftime('%Y-%m-%d-%H-%M')
	os.makedirs(f'collections/{collection_dir_name}', exist_ok=True)
	os.makedirs(f'collections/{collection_dir_name}/frames', exist_ok=True)
	DATA_FILENAME = f'collections/{collection_dir_name}/frames.txt'

	with open(DATA_FILENAME, "w") as f:
		pass
	
	frame_counter = 0

	print('Press enter or spacebar to capture a scan. Press q to finish scan session.')

	while True:
		key_event = keyboard.read_event()

		if key_event.event_type == keyboard.KEY_DOWN:
			if key_event.name == 'space' or key_event.name == 'enter':
				print("Scanning...")
				scan_frame_data = lidar_stream.get_latest_measurements()
				
				with open(DATA_FILENAME, "a") as f:
					scan_frame_data_string = str(scan_frame_data)
					f.write(f'{scan_frame_data_string}\n')
				
				print("Plotting...")
				# Create a new frame of scan data
				frame_data = format_scan_data(scan_frame_data)
				frame = Frame(frame_data, 0.1)
				frame.plot() # Plot distance measurements to x,y coordinates

				frame_filepath = f'collections/{collection_dir_name}/frames/'
				frame_filename = f'frame-{frame_counter}'
				frame.draw(filepath = frame_filepath, filename = frame_filename) # Generate scan preview image
				
				frame_counter += 1

				print('Scan capture finished. Move to the next location.')
			elif key_event.name == 'q':
				print("Exiting...")
				break  # Exit the loop

	lidar_stream.stop()

if __name__ == '__main__':
	main()