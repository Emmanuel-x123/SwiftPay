$(document).ready(function() {
    $('#personal-form').on('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting

        const $btnText = $('#btn-text');
        const $spinner = $('.spinner-border');
        const $btnPersonal = $('#btn-personal');

        $btnText.text('Loading...'); // Update the button text
        $spinner.show(); // Show the spinner
        $btnPersonal.prop('disabled', true).css({
            'background-color': '#7261f3', 
            'cursor': 'not-allowed'
        }); // Disable the button after click

        const $entireForm = $(this); // 'this' refers to the form element
        const csrfToken = $('input[name= "csrfmiddlewaretoken"]').val();
      
      
      


        $.ajax({
            type: 'POST',
            url: '/register',
            datatype: 'json',
            data: $entireForm.serialize(),
            headers: {
                'X-CSRFToken': csrfToken
            },

            success: function(res) {
                console.log('Registration successful');
                $btnText.text('Register Now'); // Reset button text
                $spinner.hide(); // Hide spinner
                $btnPersonal.prop('disabled', false).css({
                    'background-color': '', // Reset background color
                    'cursor': '' // Reset cursor
                });

                // Show success message to the user
                iziToast.success({
                    title: 'Success',
                    message: res.success,
                    position: 'topCenter'
                });

                setTimeout(function() {
                    console.log('redirect noww')
                     window.location.href = '/email_verify'; // Corrected syntax
                    }, 2000);
            },

            
            error: function(res) {
                $btnText.text('register now')
                $spinner.hide()
                $btnPersonal.prop('disabled', false).css({
                    'background-color': '',
                    'cursor': ''
                })


                iziToast.error({
                title: 'Error',
                message: res.responseJSON.error,
                position: 'topCenter'
                });               
              
            }
        })
    });


    //business registration logit starts here
    $('#business-form').on('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting

        const $btnText = $('#btnbusiness-text');
        const $spinner = $('.spinner-border');
        const $btnPersonal = $('#btn-business');

        $btnText.text('Loading...'); // Update the button text
        $spinner.show(); // Show the spinner
        $btnPersonal.prop('disabled', true).css({
            'background-color': '#7261f3', 
            'cursor': 'not-allowed'
        }); // Disable the button after click

        const $entireForm = $(this); // 'this' refers to the form elemen



        $.ajax({
            type: 'POST',
            url: '/register',
            datatype: 'json',
            data: $entireForm.serialize(),

            success: function(res) {
                console.log('Registration successful');
                $btnText.text('Register Now'); // Reset button text
                $spinner.hide(); // Hide spinner
                $btnPersonal.prop('disabled', false).css({
                    'background-color': '', // Reset background color
                    'cursor': '' // Reset cursor
                });

                // Show success message to the user
                iziToast.success({
                    title: 'Success',
                    message: res.success,
                    position: 'topCenter'
                });

                    // Redirect to email verification page after 2 seconds
            },

            
            error: function(res) {
                $btnText.text('register now')
                $spinner.hide()
                $btnPersonal.prop('disabled', false).css({
                    'background-color': '',
                    'cursor': ''
                })


                iziToast.error({
                title: 'Error',
                message: res.responseJSON.error,
                position: 'topCenter'
                });               
              
            }
        })
    });

    $('#loginPersonal-form').on('submit', function(e) {
        e.preventDefault()

        const $btnText = $('#btn-text');
        const $spinner = $('.spinner-border');
        const $btnPersonal = $('#btn-personal');

        $btnText.text('Loading...'); // Update the button text
        $spinner.show(); // Show the spinner
        $btnPersonal.prop('disabled', true).css({
            'background-color': '#7261f3', 
            'cursor': 'not-allowed'
        }); // Disable the button after click

        const $entireForm = $(this);
        const csrfToken = $('input[name= "csrfmiddlewaretoken"]').val();


        $.ajax({
            type: 'POST',
            url: '/login',
            datatype: 'json',
            data: $entireForm.serialize(),
            headers: {
                'X-CSRFToken': csrfToken
            },

            success: function(res) {
                console.log('Registration successful');
                $btnText.text('Register Now'); // Reset button text
                $spinner.hide(); // Hide spinner
                $btnPersonal.prop('disabled', false).css({
                    'background-color': '', // Reset background color
                    'cursor': '' // Reset cursor
                });

                // Show success message to the user
                iziToast.success({
                    title: 'Success',
                    message: res.success,
                    position: 'topCenter'
                });

                setTimeout(function() {
                    console.log('redirect noww')
                     window.location.href = '/'; // Corrected syntax
                    }, 2000);
            },

            error: function(res) {

                $btnText.text('login now')
                $spinner.hide()
                $btnPersonal.prop('disabled', false).css({
                    'background-color': '',
                    'cursor': ''
                })


                iziToast.error({
                title: 'Error',
                message: res.responseJSON.error,
                position: 'topCenter'
                });               
              
            }

           
        })

        
      
        
    })


});
