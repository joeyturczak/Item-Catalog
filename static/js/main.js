// Source: Udacity's Authentication and Authorization course
function signInCallback(authResult) {
  toggleProgress(true);
  if(authResult['code']) {
    // Hide the sign-in button now that the user is authorized
    $('signinButton').attr('style', 'display:none');
    // Send the one-time-use code to the server, if the server
    // responds, write a 'login successful' message to the web
    //page and then redirect back to the main catalog page
    $.ajax({
      type: 'POST',
      url: '/gconnect?state=' + $('#signinButton').data("state"),
      processData: false,
      contentType: 'application/octect-stream; charset=utf-8',
      data: authResult['code'],
      success: function(result) {
        toggleProgress(false);
        if(result) {
          $('#result').html('Login Successful!</br>'+ result + '</br>Redirecting...')
          setTimeout(function() {
            window.location.href = "/catalog";
          }, 0);
        } else if(authResult['error']) {
          console.log('There was an error: ' + authResult['error']);
        }
      }
    });
  } else {
    toggleProgress(false);
    $('#result').html('Failed to make a server-side call. Check your configuration and console.');
  }
}

function toggleProgress(toggle) {
  var progressBar = document.getElementById('progress-bar');
  if(toggle) {
    // if (progressBar.style.display === 'none') {
      progressBar.style.display = 'block';
    // }
  } else {
    // if (progressBar.style.display === 'block') {
      progressBar.style.display = 'none';
    // }
  }
}
