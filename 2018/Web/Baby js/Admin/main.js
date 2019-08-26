function Validate() {
    var u = document['getElementById']('usrname')['value'];
    var p = document['getElementById']('psw')['value'];
    if (u == 'admin' && p == '@dm1n') {
        document['location'] = document['location']['href']  + 'flag'
    } else {
        alert('Wrong username and password.Try again')
    }
}
