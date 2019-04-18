function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
$(document).ready(function()
{
    var user_='';
    $(".user_online").click(function()
    {
        user_=$(this).attr("data-value");
        $("#user_id").html(user_).show();
        $("#div_msg").show();
        $("#myDiv").show();
        $("#input_field").show();
        $("#close").show();
        $("#user_icon").show();
        $("#users_").hide();
    });
    $("#close").click(function()
    {
        $("#div_msg").hide();
        $("#myDiv").hide();
        $("#input_field").hide();
        $("#user_id").hide();
        $("#close").hide();
        $("#user_icon").show();
        $("#users_").show();
    });
    $("#msg_submit").click(function()
    {
        var message=$("#msg").val();
        if (message == '')
        {
            alert('type somthing in message field....');
            // return;
        }
        else
        {
            var type_message=$("#msg").val();
            var requs_user=$("#req_name").attr("data-value");
            // alert(requs_user);
            $.ajax({
                url: '/post_message/',
                type: 'POST',
                data: {
                    msgbox: type_message,
                    reciver:user_,
                    sender:requs_user,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
               success: function(){
                    alert("Saved Data!");
                     $("#msg").val("");
                }
            });
        }
    });
});