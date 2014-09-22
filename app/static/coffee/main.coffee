$ = jQuery

$(document).ready ->
  phraseField = $("#phrase")
  phraseText = phraseField.val()
  console.log(phraseText)
  
  $(".choosable").click ->
    oldValue = phraseField.val()
    if oldValue isnt ""
      oldValue += " "
    phraseField.val( oldValue + $(this).text().replace(/\s+/g, '').replace(/[\.,\/#!?$%\^&\*;:{}=\_"`~()]/g,"") )
    
  $("#clearphrase").click ->
    phraseField.val("")

