<script type="text/javascript">
  $(function(){
    $("#update_log_button").click(function(){
        $.post(
         url : "/register/resend",
         dataType:"html",
         success: alert('Log has been sent')
        );
        return false;
    });
 });
</script>