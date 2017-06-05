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

  /* append/prepend */
  firstLi = $('#jqul').first();
  firstLi.prepend('<li>prepend</li>');
  firstLi.append('<li>append</li>');

  /* insertBefore/After */
  toInsertBefore =  $('<li>liInsertBefore</li>');
  toInsertAfter =  $('<li>liInsertAfter</li>');
  toInsertBefore.insertBefore($('#testitem'));
  toInsertAfter.insertAfter($('#testitem'));
  $('.classitem').after('<li>liAfterClass</li>');
  $('.classitem').before('<li>liBeforeClass</li>');

  /* each */
  $('li').each(function(){
    $(this).text($(this).text()+'+each');
  });

  //parents = articleList.parents('div');     /*list all div tags in parents of article*/
  //kids = articleList.find('*') /*or*/ articleList.children();     /*find all children of article*/
  //h1 = articleList.siblings('h1');     /*find all tags of h1 in siblings*/
  //articleList = $('.article-list');     /*returns jQ DOM object*/



  /*
  [jQ CDN]
  https://developers.google.com/speed/libraries/#jquery
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  [jQ]
  $ === jQuery returns "function (a,b){return new n.fn.init(a,b)}"
  */

});
