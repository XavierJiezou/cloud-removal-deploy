$('#inputfile').bind('change', function() {
    let fileSize = this.files[0].size/1024/1024; // this gives in MB
    if (fileSize > 1) {
      $("#inputfile").val(null);
      alert('file is too big. images more than 1MB are not allowed')
      return
    }

    let ext = $('#inputfile').val().split('.').pop().toLowerCase();
    if($.inArray(ext, ['jpg','jpeg','png']) == -1) {
      $("#inputfile").val(null);
      alert('only jpeg/jpg files are allowed!');
    }

    var imgFile = this.files[0];
    var fr = new FileReader();
    fr.onload = function() {
        $('#imgShowHere').attr('src', fr.result)
        $('#out').attr('src', '/static/img/uploadBg.png')
    }
    fr.readAsDataURL(imgFile);
});


$('#upload').click(function(){
    var targetUrl = $("#form").attr("action");
    var data = new FormData($("#form")[0])
    $.ajax({
        type: "post",
        url: targetUrl,
        cache: false,
        processData: false,
        contentType: false,
        data: data,
        dataType: "json",
        success: function(res){
          $('#out').attr('src', res.outdir+'?'+Math.random())
        },
        error: function(err){
            console.log(err)
        }
    })
})