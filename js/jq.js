/*functions run after DOM load finish*/
$(function(){

  /*[jQ selector]*/
  let li = $('li');     /*return list of ALL li*/
  console.log('@allitem',li);
  let classitem = $('.classitem');     /*list of all class, same as CSS selector*/
  console.log('@classitem',classitem.html());
  let testitem = $('#testitem');     /*single element, unique*/
  console.log('@testitem',testitem.text());

  /* DOM manipulation */
  let featured = $('.featured').toggleClass('featured'); /*set and unset a class*/
  console.log('@featured',featured);

  /* class toggle */
  article2 = $('.featured');
  article3 = featured.next(); /* select the next sibling*/
  article2.toggleClass('featured');
  article3.toggleClass('featured');
  console.log('@article3',article3);

  /* get/set attr */
  let li1Id = $('#testitem').attr('href'); /* get attr */
  console.log('@getAttr',li1Id);
  $('#testitem').attr('href','#link'); /* set attr */
  console.log('@afterSetAttr',$('#testitem').attr('href'));

  /* css mod */
  classitem.css('background-color','red');
  console.log('@css style mod',classitem.attr('style'));

  /* element text mod */
  $('#input').on('change', function() {
      let val = $('#input').val();
      $('h1').text(val);
  });

  /* remove element */
  $('#rm').remove();

  /* append/prepend create children*/
  firstLi = $('#jqul').first();
  firstLi.prepend('<li>prepend</li>');
  firstLi.append('<li>append</li>');

  /* insertBefore/After create siblings*/
  toInsertBefore =  $('<li>liInsertBefore</li>');
  toInsertAfter =  $('<li>liInsertAfter</li>');
  toInsertBefore.insertBefore($('#testitem'));
  toInsertAfter.insertAfter($('#testitem'));
  $('.classitem').after('<li>liAfterClass</li>');
  $('.classitem').before('<li>liBeforeClass</li>');

  /* each, modify list of ele*/
  $('li').each(function(){
    $(this).text($(this).text()+'+each');
  });

  //parents = articleList.parents('div');     /*list all div tags in parents of article*/
  //kids = articleList.find('*') /*or*/ articleList.children();     /*find all children of article*/
  //h1 = articleList.siblings('h1');     /*find all tags of h1 in siblings*/
  //articleList = $('.article-list');     /*returns jQ DOM object*/

  /* monitor event */
  /*monitorEvents() only avaialbe in Chrome dev tool
  */

  /*
  jQ event listner
  */
  /* click button turns purple */
  $('#my-button').on('click',function(e){
    console.log(e);
    //$(this).remove();
    $(e.target).css('background-color','purple');
    $('body').attr('class','success');
  });
  /* overwrite a-href to log and not redirect */
  $('#fakelink').on('click',function(e){
    e.preventDefault(); /*precent default redirect*/
    console.log('fakelink clicked');
  });
  /* other events
  event.keyCode: to learn what key was pressed
  event.pageX/pageY: where on the page the click occurred
  event.type: to find what event happened if listening to a target for multiple events
  https://api.jquery.com/category/events/event-object/
  https://api.jquery.com/event.target/
  http://www.w3.org/TR/DOM-Level-3-Events/
  The Convenience Method http://api.jquery.com/category/events/
  */
  /*event delegation
      add event to non-exist elements
  */
  /* add a new li to jqul */
  $( '#add-li' ).on( 'click', function(e) {
    newLi = "<li>new li</li>";
    $('#jqul').append(newLi);
  });
  /* add event to any li in jqul, click turns pink */
  $( '#jqul' ).on( 'click', 'li', function(e) {
    $(e.target).css('background-color','pink');
  });

  /*
  [jQ CDN]
  https://developers.google.com/speed/libraries/#jquery
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  [jQ]
  $ === jQuery returns "function (a,b){return new n.fn.init(a,b)}"
  */

});
