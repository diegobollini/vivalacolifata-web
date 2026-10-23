(function () {
  "use strict";

  if (!("querySelector" in document) || !("fetch" in window)) {
    return;
  }

  var audio = document.getElementById("stream");
  var notice = document.getElementById("stream-offline");
  if (!audio || !notice) {
    return;
  }

  // SonicPanel status endpoint: CORS-enabled, bitrate is "0" when no source is connected
  var statusUrl = "https://radios.solumedia.com/cp/get_info.php?p=6076";
  var checkInterval = 60000;

  function showStatus(online) {
    // The theme sets audio{display:inline-block}, which overrides the hidden attribute
    audio.style.display = online ? "" : "none";
    notice.hidden = online;
    if (!online && !audio.paused) {
      audio.pause();
    }
  }

  function checkStream() {
    fetch(statusUrl, { cache: "no-store" })
      .then(function (response) {
        return response.json();
      })
      .then(function (info) {
        showStatus(Number(info.bitrate) > 0);
      })
      .catch(function () {
        // Keep the player visible if the status endpoint is unreachable
      });
  }

  // The stream URL serves an HTML page instead of audio while offline
  audio.addEventListener(
    "error",
    function () {
      showStatus(false);
    },
    true,
  );

  checkStream();
  window.setInterval(checkStream, checkInterval);
})();
