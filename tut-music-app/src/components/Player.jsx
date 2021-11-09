import React, { useRef, useEffect, useState } from "react";
import PlayerDetail from "./PlayerDetail";
import PlayerController from "./PlayerController";
function Player({ songs, nextSong, setCurrentSongIndex, currentSontIndex,nextSongIndex }) {
  const audioEl = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  useEffect(() => {
    if (isPlaying) {
      audioEl.current.play();
    } else {
      audioEl.current.pause();
    }
  });
  const skipSong = (forward = true) => {
    if (forward) {
      setCurrentSongIndex(() => {
        let temp = currentSontIndex;
        temp++;
        if (temp > songs.length - 1) {
			temp = 0
        }
		return temp
      });
    } else {
		setCurrentSongIndex(() => {
			let temp = currentSontIndex
			temp--
			if (temp < 0){
				temp = songs.length -1
			}
			return temp
		})
    }
  };
  return (
    <div className="c-player">
      <audio ref={audioEl}src={songs[currentSontIndex].src} ></audio>
      <h4>Playing now</h4>
      <PlayerDetail song={songs[currentSontIndex]} />
      <PlayerController />
      <p>
        <strong>Next up:</strong>
        {songs[nextSongIndex].title} by {songs[nextSongIndex].artist}
      </p>
    </div>
  );
}

export default Player;
