from music_player import trim_song_name
import pytest

def test_trim_song_name():
    # trim length
    MAX_LEN = 20
    # list of untrimmed song names
    song_names = [
        '06 Come Thou Fount (feat. Paul Carda).mp3',
        '09 Homeward Bound.mp3',
        'The_Temperature_of_the_Air_on_the_Bow_of_the_Kaleetan.mp3',
        'Gabriel Rios - Gold (Thomas Jack Remix).mp3',
        'melody.mp3'
    ]
    # list of corresponding trimmed names. names are trimmed to max_len = 20
    trimmed_names = [
        '06 Come Thou Fount (...',
        '09 Homeward Bound',
        'The_Temperature_of_t...',
        'Gabriel Rios - Gold ...',
        'melody'
    ]
    for i in range(len(song_names)):
        assert trim_song_name(song_names[i], MAX_LEN) == trimmed_names[i]


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])