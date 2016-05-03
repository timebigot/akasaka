$('#imager').on('show.bs.modal', function (event) {
    var anchor = $(event.relatedTarget) // Button that triggered the modal
    var name = anchor.data('name')
    var price = anchor.data('price')
    var image = anchor.data('image')
    var modal = $(this)
    modal.find('.item-name').text(name)
    modal.find('.item-price').text(price)
    modal.find('.modal-body img').attr('src', image)
})
