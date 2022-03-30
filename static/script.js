function btn() {
    let txt = $('#input').val();
    let temp_html =
        `<p id="delete"><input type="checkbox" >  ${txt}
        <button onclick="del()" class="btn-del">del</button></p>`

    if (txt == "") {
        alert("리스트가 없습니다.")
    } else {
        $('#checkbox').append(temp_html);
        let input = document.getElementById("input");
        input.value = null;
    }
}

function del() {
    $('#delete').remove();
}