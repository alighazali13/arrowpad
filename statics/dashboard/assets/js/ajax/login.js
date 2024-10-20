// Checks if a string contains only numbers
function containsOnlyNumbers(str) {
    return /^\d+$/.test(str);
};


document.getElementById('reqlogin_code_BTN').addEventListener('click', function() {
    const phoneNumber = document.getElementById('tel').value;
    if (containsOnlyNumbers(phoneNumber) == true && phoneNumber.length == 10 ) {
        console.log(phoneNumber)
        const data = {
            'protocol' : 'validation',
            'phoneNumber' : phoneNumber,
        };

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                // if not safe, set csrftoken
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
                };
            }
        });
        // Sending data from validation
        $.ajax({
            url : '/a/d/min/strator/signin/valvalidation/' ,
            type : "POST" ,
            data : {
                'getdata' : JSON.stringify(data)
            } ,
            dataType : 'json' ,
            success : function (res , status) {
                console.log(res.status);
                if (res.status == 200){
                    console.log(res.status)
                    cf = '<input type="hidden" id="p" value="'+res.phoneNumber+'">'+
                         '<div class="form-group">'+
                             '<input autocomplete="off" id="code" type="text" name="code" placeholder=" کد ارسال شده را وارد کنید " class="form-control" required>'+
                         '</div>'+
                         '<div class="form-group d-flex justify-content-center">'+
                             '<button onclick="cb()" id="code_BTN" type="button" name="code_BTN" class="btn btn-primary">ورود</button>'+
                         '</div>'
                    document.getElementById('pn').remove();
                    $('#form').append(cf);
                }if (res.status == 404) {
                    console.log(res.status)
                    document.getElementById('custom_alert').classList.remove('d-none');
                    document.getElementById('custom_alert').classList.add('d-block');
                    document.getElementById('custom_alert').classList.add('position-absolute');
                    document.getElementById('msg').innerHTML = res.msg;
                }
            } ,
            error : function () {
                console.log('er')
                
            } ,
        });
    }else{
        var msg = 'مقدار رمز عبور نمی توانند خالی باشد .'
        var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + msg + '</div>'
        $('#validation_msg').append(alert);
    }
});

function cb() {
    const code = document.getElementById('code').value;
    console.log(code)
    if (containsOnlyNumbers(code) == true && code.length == 5 ) {
        var phoneNumber = document.getElementById('p').value;
        const data = {
            'protocol' : 'code',
            'code' : code,
            'phoneNumber' : phoneNumber,
        };

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                // if not safe, set csrftoken
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
                };
            }
        });
        // Sending data from validation
        $.ajax({
            url : '/a/d/min/strator/signin/valvalidation/' ,
            type : "POST" ,
            data : {
                'getdata' : JSON.stringify(data)
            } ,
            dataType : 'json' ,
            success : function (res , status) {
                console.log(res.status);
                if (res.status == 200) {
                    console.log(res.status)
                    window.location.href = res.url;
                }
                
                if (res.status == 500) {
                    console.log(res.status)
                    document.getElementById('custom_alert').classList.remove('d-none');
                    document.getElementById('custom_alert').classList.add('d-block');
                    document.getElementById('custom_alert').classList.add('position-absolute');
                    document.getElementById('msg').innerHTML = res.msg;
                }
            } ,
            error : function () {
                console.log('er')
                
            } ,
        });
    }else{
        var msg = 'مقدار رمز عبور نمی توانند خالی باشد .'
        var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + msg + '</div>'
        $('#validation_msg').append(alert);
    }
}

    

