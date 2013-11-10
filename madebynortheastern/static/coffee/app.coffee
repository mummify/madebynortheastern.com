

$('document').ready ->
  console.log 'everything is good'

  last = null

  $('ul.companies li').click (e) ->
    do e.preventDefault
    $(last).removeClass('card-visible') if last?
    el = $(e.currentTarget)
    $(el).addClass 'card-visible'
    last = el

  $('a.hide').click (e) ->
    do e.stopPropagation
    console.log $(this).parents('li.card-visible')
    $(this).parents('li.card-visible').removeClass 'card-visible'



$(window).scroll ->
  if $(window).scrollTop() > 100
    $(".sticky-logo").addClass 'fixed'
  else
    $(".sticky-logo").removeClass 'fixed'


