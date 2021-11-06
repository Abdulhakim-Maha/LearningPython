import React from 'react'
import PlayerDetail from './PlayerDetail'
import PlayerController from './PlayerController'
function Player({song, nextSong}) {
	return (
		<div className='c-player'> 
			<audio></audio>	
			<h4>Playing now</h4>
			<PlayerDetail song={song}/>
			<PlayerController  />
			<p><strong>Next up:</strong>{nextSong.title} by {nextSong.artist}</p>
		</div>
	)
}

export default Player
