$ = jQuery

$(document).ready ->
  phraseField = $("#phrase")
  
  $(".choosable").click ->
    oldValue = phraseField.val()
    if oldValue isnt ""
      oldValue += " "
    phraseField.val( oldValue + $(this).text().replace(/\s+/g, '').replace(/[\.,\/#!?$%\^&\*;:{}=\_"`~()]/g,"") )
    
  $("#clearphrase").click ->
    phraseField.val("")

  $("#submit_phrase").click ->
    resp = $("#addphrase_response")
    $.ajax 
      url: '/ajax_add_phrase',
      type: 'POST',
      data: 
        phrase: $('#phrase').val()
        tense: $('#tense').val()
        url: location.href
        
      success: (data, textStatus, jqXHR) ->
        json = JSON.parse(data)
        resp.empty()
        resp.append (json["statustext"])
        
        if resp.hasClass("alert-danger") == true
          resp.removeClass("alert-danger")
        if resp.hasClass("alert-success") == true
          resp.removeClass("alert-success")
        if resp.hasClass("alert-warning") == true
          resp.removeClass("alert-warning")
          
        if json["status"] == "already_exists"
          resp.addClass("alert-warning")
        else
          resp.addClass("alert-success")
          $('#phrase').val("")
          
        resp.hide().fadeIn(500).delay(2000).fadeOut(1500)
        # console.log(data)
        
        
      error: (jqXHR, textStatus, errorThrown) ->
        resp.empty()
        resp.append ("Error")
        
        if resp.hasClass("alert-success") == true
          resp.removeClass("alert-success")
        if resp.hasClass("alert-warning") == true
          resp.removeClass("alert-warning")
          
        resp.addClass("alert-danger")
        
