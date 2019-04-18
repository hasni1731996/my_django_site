$(document).ready(function(){
    $('#btn_submit').on('click', function(){
        $firstname = $('#firstname').val();
        $lastname = $('#lastname').val();
        $age = $('#age').val();
        $address = $('#address').val();

        if($('#firstname').val() == "" || $('#lastname').val() == "" || $('#age').val() == "" || $('#address').val() == ""){
            alert("Please fill up the required field");
        }else{
            $.ajax({
                type: "POST",
                url : "insert",
                data: {
                    firstname: $firstname,
                    lastname: $lastname,
                    age: $age,
                    address: $address,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    alert("Saved Data!");
                    $('#firstname').val('');
                    $('#lastname').val('');
                    $('#age').val('');
                    $('#address').val('');
                }
            });
        }

    });
});