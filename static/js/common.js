function email_send(id, data) {
  $(id).submit(function (event) {
    event.preventDefault();
    $(this).validate();
    var requestData = Object.assign({}, data);
    var $inputs = $(this).find('input, textarea, select');
    $inputs.each(function () {
      requestData[this.name] = $(this).val();
    });
    $.ajax({
      url: '/ajax/send/email/',
      type: 'post',
      data: JSON.stringify(requestData),
      dataType: 'text',
      contentType: "application/json",
      success: function () {
        $.notify({
          message: "Ваша заявка успешно оформлена"
        }, {
          type: 'success'
        });
        $inputs.each(function () {
          $(this).val('');
        });
        $('.selectpicker').selectpicker('val', '');
      },
      error: function () {
        $.notify({
          message: "Извините, произошла ошибка на стороне сервера"
        }, {
          type: 'danger'
        });
      }
    });
  });
}