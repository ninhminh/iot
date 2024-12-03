function Login()
{
    console.log("đăng nhập");
    const xhttp = new XMLHttpRequest();
    var email = document.getElementById('email').value;
    //  Lấy giá trị trong element input với id là password:
    var password = document.getElementById('password').value;
    xhttp.onload = function()
        {
            alert("đăng nhập")
            //lấy dữ liệu dạng json
            var ResponseJson=xhttp.responseText
            //chuyển về dữ liệU javascript
            var Response= JSON.parse(ResponseJson)
            if(xhttp.status==201)
            {
                //vứi status =201 thành công
                alert("Đăng nhập thành công");
                localStorage.setItem('userID',Response['ID']);
                window.location = "/Main";
                
                console.log("Đăng nhập thành công")
            }
            else{
                var s = document.getElementById('error-message')
                var s1 = '<p>'+Response["Vui lòng nhập lại"]+'</p>';
                s.innerHTML = s1;
            }
        }     
        const userInfo={
            email:email,
            password:password
        }
        postUser=JSON.stringify(userInfo);
        //khai báo phương thức và đường dẫn để request
        xhttp.open("POST","/Apiv1/login/",false);
        //định dạng gửi đi787
        xhttp.setRequestHeader("Content-type","application/json")
        //gửi
        xhttp.send(postUser);    
}