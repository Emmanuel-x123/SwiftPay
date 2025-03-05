$(document).ready(function(){
    $('#verifyForm').on('submit', function(e){
        e.preventDefault()
        const $form = $(this)
        const $btnText = $('#btnVerify-text');
        const $spinner = $('.spinner-border');
        const $btnVerify = $('#btn-verify');


        $btnText.text('Verifying...')
        $spinner.show(); // Show the spinner
        $btnVerify.prop('disabled', true).css({
            'background-color': '#7261f3', 
            'cursor': 'not-allowed'
        
    })

    const csrfToken = $('input[name= "csrfmiddlewaretoken"]').val();


    $.ajax({
        type: 'POST',
        url: '/email_verify',
        datatype: 'json',
        data: $form.serialize(),
        datatype: 'json',
        headers: {
            'X-CSRFToken': csrfToken
        },

        success: function(res) {
            $form[0].reset();
            $btnText.text('Verify now'); // Reset button text
            $spinner.hide(); // Hide spinner
            $btnVerify.prop('disabled', false).css({
                'background-color': '', // Reset background color
                'cursor': '' // Reset cursor
            });

            // Show success message to the user
            iziToast.success({
                title: 'Success',
                message: res.success,
                position: 'topCenter'
            });

            // setTimeout(function() {
            //     console.log('redirect noww')
            //      window.location.href = '/email_verify'; // Corrected syntax
            //     }, 2000);
        },

        
        error: function(error) {
            $form[0].reset();
            $btnText.text('Verify Now')
            $spinner.hide()
            $btnVerify.prop('disabled', false).css({
                'background-color': '',
                'cursor': ''
            })

            // console.log(error.responseJSON.error)


            iziToast.error({
            title: 'Error',
            message: error.responseJSON.error,
            position: 'topCenter'
            });               
          
        }
    })
    })

});