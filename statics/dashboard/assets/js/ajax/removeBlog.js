
function removeBlog(adminDisplayName) {
    const title = document.getElementById('id_title').value;
    
    
    const data = {
        'adminDisplayName' : adminDisplayName,
    };
    console.log(data)
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
        url : '/a/d/min/strator/remove/<str:en_name>/<str:url>' ,
        type : "POST" ,
        data : {
            'getdata' : JSON.stringify(data)
        } ,
        dataType : 'json' ,
        success : function (res , status) {
            console.log('success');
            
        } ,
        error : function () {
            console.log('error')
            
        } ,
    });
}
    