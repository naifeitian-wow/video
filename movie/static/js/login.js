$(function () {
    var user_error = true;
    var password_error = true;
    $('.name_input').blur(function () {
        if ($(this).val()==''){
            $('.user_error').html('请输入用户名').show();
            user_error=true;
        }
        else{
            $('.user_error').hide()
            user_error=false;
        }
    })
    $('.pass_input').blur(function () {
        if ($(this).val()==''){
            $('.pwd_error').html('请输入密码').show()
            password_error=true;
        }
        else{
            $('.pwd_error').hide()
            password_error=false;
        }
    })

    $('form').submit(function(){
        name=$('.name_input').val().length
        password=$('.pass_input').val()
        if(name==0){
            user_error=true
        }
        if(password==''){
            password_error=true
        }
        if(user_error==false && password_error==false){
            // 只有用户和密码输入框同时输入的时候才不阻止提交
            return true
        }else{
            return false
        }

    })


      // if($('#is_user').text=='0'){
      //     $('.user_error').html('账号错误').show()
      // }
      // if($('#is_password').text=='0'){
      //     $('.pwd_error').html('密码错误').show()
      // }

})