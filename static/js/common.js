/*
* @Author: cecile
* @Date:   2018-09-07 09:06:06
* @Last Modified by:   cecile
* @Last Modified time: 2018-10-19 09:20:00
*/
$(function() {
    // 如果鼠标移到行上时，执行函数    
    $(".table tr").mouseover(function() {
        $(this).css({background : "#CDDAEB"});
        $(this).children('td').each(function(index, ele){
            $(ele).css({color: "#1D1E21"});
        });
    }).mouseout(function() {
        $(this).css({background : "#FFF"});
        $(this).children('td').each(function(index, ele){
            $(ele).css({color: "#909090"});
        });
    });
});

function selectOrClearAllCheckbox(){
    var all_check = document.getElementById("all_checkbox");
    var one_check = document.getElementsByName("article_check");
    if(all_check.checked==true){
        for(var i=0; i<one_check.length; i++){
            one_check[i].checked = true;
        }
    }
    else{
        for (var i=0; i<one_check.length; i++) {
            one_check[i].checked = false;
        }
    }
}

function rem_confirm(articleid){
    var r=confirm("确定删除？");
    if (r==true){
        window.open(articleid+"/rem/",'articlerem')
    } 
}

kt_rem_confirm = function (ktid) {
    var r=confirm("确定删除？");
    if (r==true){
        window.open(ktid+"/rem/", 'ktrem')
    }
}

function batch_rem_confirm(){
    var articles = document.getElementsByName("article_check");
    var check_flag = false;
    for (var i=0; i<articles.length; i++){
        if(articles[i].checked==true){
            check_flag = true;
            var r=confirm("确定删除？");
            if (r==true){
                $("#articles_check").submit();
                //$.post("papers/del/", $("#paper_check").serialize());
            }
            break;
        }
    }
    if (check_flag == false){
        alert("请选择需删除的条目！");
    }   
}

ktBatchRemConfirm = function (){
    var kts = document.getElementsByName("kt_check");
    var check_flag = false;
    for (var i=0; i<kts.length; i++){
        if (kts[i].checked==true){
            check_flag = true;
            var r=confirm("确定删除？");
            if (r==true){
                $("#kts_check").submit();
            }
            break;
        }
    }
    if (check_flag == false){
        alert("请选择需删除的条目！");
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
    var csrftoken = getCookie('csrftoken');     
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

