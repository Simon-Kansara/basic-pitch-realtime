# basic-pitch-realtime

This Python script records audio in real-time, performs inference using the [basic-pitch model from Spotify Labs](https://github.com/spotify/basic-pitch), and sends the detected note events via OSC (Open Sound Control).

## Dependencies

*   time
*   numpy
*   sounddevice
*   scipy.io.wavfile
*   tempfile
*   os
*   pythonosc
*   basic_pitch

You can install the necessary dependencies with pip:

```bash
pip install numpy sounddevice scipy python-osc basic-pitch
```

## Usage

1.  Make sure you have installed the required dependencies and Python 3.10.
2.  Run the script:

    ```bash
    python basic-pitch-realtime.py
    ```
3.  The script will display a list of available audio devices and prompt you to choose an input device. Enter the index of the desired device.
4.  The script will then record audio, perform inference, and send the note events via OSC.
5.  To stop the script, press Ctrl+C.

## Configuration

The following parameters can be configured in the script:

*   `OSC_IP`: The IP address to send OSC messages to (default: `"127.0.0.1"`).
*   `OSC_PORT`: The port to send OSC messages to (default: `8000`).
*   `SAMPLE_RATE`: The sampling rate of the audio (default: `22050`).
*   `DURATION`: The duration of the audio recording in seconds (default: `1.0`).

You can modify these parameters directly in the script.
