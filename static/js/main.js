// Source: Udacity's Authentication and Authorization course
function signInCallback(authResult) {
  // window.location.href = "/login";
  toggleProgress();
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
        toggleProgress();
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
    toggleProgress();
    $('#result').html('Failed to make a server-side call. Check your configuration and console.');
  }
}

// function onSignIn(googleUser) {
//   if(authResult['code']) {
//     // Hide the sign-in button now that the user is authorized
//     $('signinButton').attr('style', 'display:none');
//     // Send the one-time-use code to the server, if the server
//     // responds, write a 'login successful' message to the web
//     //page and then redirect back to the main catalog page
//     $.ajax({
//       type: 'POST',
//       url: '/gconnect?state=' + $('#signinButton').data("state"),
//       processData: false,
//       contentType: 'application/octect-stream; charset=utf-8',
//       data: authResult['code'],
//       success: function(result) {
//         if(result) {
//           $('#result').html('Login Successful!</br>'+ result + '</br>Redirecting...')
//           setTimeout(function() {
//             window.location.href = "/catalog";
//           }, 0);
//         } else if(authResult['error']) {
//           console.log('There was an error: ' + authResult['error']);
//         }
//       }
//     });
//   } else {
//     $('#result').html('Failed to make a server-side call. Check your configuration and console.');
//   }
// }
//
// function signOut() {
//   var auth2 = gapi.auth2.getAuthInstance();
//   auth2.signOut().then(function () {
//     console.log('User signed out.');
//   })
// }

function toggleProgress() {
  var progressBar = document.getElementById('progress-bar');
  if (progressBar.style.display === 'none') {
    progressBar.style.display = 'block';
  } else {
    progressBar.style.display = 'none';
  }
}
