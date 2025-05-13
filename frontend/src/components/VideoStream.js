import React, { useEffect, useRef } from 'react';

const VideoStream = () => {
  const videoRef = useRef(null);

  useEffect(() => {
    videoRef.current.src = 'http://localhost:5000/video';
  }, []);

  return (
    <div>
      <h2>Live ASL Detection</h2>
      <img ref={videoRef} alt="Live Stream" width="640" height="480" />
    </div>
  );
};

export default VideoStream;
