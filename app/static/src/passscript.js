

function platformsubmit(event){
    platform=document.getElementById("platform").value
    password=document.getElementById("spassword").value
    if (platform=="" || password==""){
      event.preventDefault();
  
      document.getElementById("Errorplt").innerHTML = "*Both the  fields are required";
  
    }
  }

  $(document).ready(function() {
  $('.clicktocopy').on('click', function(){
    var that=this
    var hash_password = $(this).parent().parent().text();
    var key = $(this).parent().parent().parent().parent().attr('id');
    $(this).parent().attr('data-tip','copied')
    $(this).attr('stroke','cyan')
  
    setTimeout(function(){
      $(that).parent().attr('data-tip','copy');
      $(that).attr('stroke','currentcolor')
    }, 2000);
    
   

    $.ajax({
      type: 'GET',
      url:'{% url "decrypt" %}',
      data:{
          'password':hash_password,
          'decrypt_key': key
         
          
      },
      success: function(response){
        var res=response
        console.log('created');
        console.log(response['decrypted_password'])
        navigator.clipboard.writeText(response['decrypted_password']);
      }

     
  })

});
  });
$(document).ready(function() {
$('.delete-pass').on('click', function(){
    
    
  var key_id = $(this)[0].classList[0];
   console.log(key_id)
    
  

  $('.btn-del').on('click', function(){

   

   $.ajax({
    type: 'POST',
    url:'{% url "delete-rec" %}',
    
    data:{
        'record-del':key_id,
        'csrfmiddlewaretoken':'{{ csrf_token }}'
        
    },
    success: function(){
       console.log('sucess');
       location.reload();
       
    }
})
})
});
});



