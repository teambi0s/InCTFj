function hex2a(hexx) {
    var hex = hexx.toString();//force conversion
    var str = '';
    for (var i = 0; (i < hex.length && hex.substr(i, 2) !== '00'); i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

function isalpha(char)
{
  return char.toUpperCase() != char.toLowerCase();
}

function shift_rev(str)
{
  var n = '';
  var alphs = 'abcdefghijklmnopqrstuvwxyz';
  var digit = '1234567890';
  for(var i = 0;i<str.length;i++)
  {
    var x = str.charAt(i);
    if(isalpha(x))
    {
      x = x.toLowerCase();
      if(alphs.indexOf(x) - 3 >= 0)
        n = n.concat(alphs[(alphs.indexOf(x)-3)%26]);
      else
        n = n.concat(alphs[(alphs.indexOf(x)-3 + 26)%26]);
    }
    else if(!isNaN(i))
    {if(digit.indexOf(x) - 8 >= 0)
      n = n.concat(digit[(digit.indexOf(x)-8)%10])
    else
      n = n.concat(digit[(digit.indexOf(x) - 8 + 10)%10]);
    }
  }
  return n;
}

console.log(hex2a(shift_rev(atob('NDc0aDQxNTI0NDRkNWUzMzU4NTExOTQyNDMzaTQyMTg1NTRoM2k0ZDI4NTQyODUxNDE1MDE5NTg1MjVn'))));
