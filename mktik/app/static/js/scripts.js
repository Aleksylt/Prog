$.ajax('http://127.0.0.1:8000/addr_lst',
{dataType: 'json', // type of response data
    timeout: 500,     // timeout milliseconds
    success: function (data,status,xhr) {   // success callback function
        $('p').append(data.id);
//        $('.result').append(data.firstName + ' ' + data.middleName + ' ' + data.lastName);

    },
    error: function (jqXhr, textStatus, errorMessage) { // error callback
        $('p').append('Error: ' + errorMessage);
    
    }
    });


/*
ajax.onload = function() {
        if (ajax.readyState == 4) {

            if (ajax.status == 200 || ajax.status == 304) {
                // код при успешном запросе
                document.querySelector('.result').textContent = ajax.response; // ответ сервера
            } else {
                document.querySelector('.result').textContent = "Нет связи с сервером"
                // код при ошибке
            }
        }
    }
ajax.onerror = function() {
    document.querySelector('.result').textContent = "Error";

    }
    setTimeout(executeQuery, 15000);
}

$(document).ready(function() {
  // run the first time; all subsequent calls will take care of themselves
  setTimeout(executeQuery, 5000);
});

*/