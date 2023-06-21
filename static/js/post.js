$(document).ready(function () {
    console.log("loaded");
    /**
     * Create Post
     */
    // process the form
    $('#create_postfrm').submit(function (e) {
        // console.log("Creating the post");
        e.preventDefault();
        // get the form data
        var formData = {
            'title': $('#id_title').val(),
            'content': $('#id_content').val(),
            'author': $('#id_author').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            contentType: 'application/x-www-form-urlencoded',
            encode: true,
        };
        $.ajax({
            type: 'POST',
            url: 'create/',
            data: formData,
            dataType: 'json',
        }).done(function (data) {
            $(function () {
                /**
                 * Update post view
                 */
                $('#addpost').modal('toggle').slideUp(500);
                $("#postdata").append(
                    '<tr id="post_row">' +
                    '<th scope="row">' + data.data['id'] + '</th>' +
                    '<td>' + data.data['title'] + '</td>' +
                    '<td>' + data.data['content'] + '</td>' +
                    '<td>' + data.data['author'] + '</td>' +
                    '<td>' + '<input type="button" class="delete-button btn btn-primary" ' + 'id="' + data.data['id'] + '"' + 'name="delete-button' + data.data['id'] + '" value="delete">' +
                    '</td>' +
                    '</tr>'
                )
            });
        });
    });

    /**
     * Delete Post
     */
    $(document).on('click', '.delete-button', function (e) {
        e.preventDefault();
        row = $(this).closest('tr');
        btn = e.target.id;      //get clicked button
        del_id = $(this).attr(btn);
        var formData = {
            'id': btn,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        };
        $.ajax({
            type: 'POST',       // define the type of HTTP verb we want to use (POST for our form)
            url: "delete/" + formData.id + "/",
            encode: true,
            contentType: 'application/x-www-form-urlencoded',
            crossDomain: false,
            dataType: 'json',
            data: formData,     // our data object
            success: function (data) {
                /**
                 * Update post view
                 */
                // console.log('success', data);
                row.fadeOut(1000, function () {
                    $(this).remove();
                });
            },
            error: function (exception) {
                alert('Exeption:' + exception);
            }
        });
    });
});
