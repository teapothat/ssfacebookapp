window.fbAsyncInit = function() {
    FB.init({
      appId      : '542921746076070',
      cookie     : true,
      xfbml      : true,
      version    : 'v2.2'
    });
    FB.getLoginStatus(check_login);
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


function check_login() {
    FB.getLoginStatus(function(response) {
      if (response.status === 'connected') {
        login_success(response);
      }
    });
}

function login_success(response) {
    var uid = response.authResponse.userID;
    var accessToken = response.authResponse.accessToken;
    if(document.location.href.indexOf('user') == -1) {
        window.location.href = "/user/" + uid + '?accessToken=' + accessToken;
    }
}

function logout() {
    if (confirm('Are you sure you want to logout?')) {
        FB.logout(function(response) {
            window.location.href = "/logout/"
        });
    }
}
