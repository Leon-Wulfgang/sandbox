/*[jQ selector]*/
parents = articleList.parents('div');     /*list all div tags in parents of article*/
kids = articleList .find('*') /*or*/ articleList.children();     /*find all children of article*/
h1 = articleList .siblings('h1');     /*find all tags of h1 in siblings*/
articleList = $('.article-list');     /*returns jQ DOM object*/
$('#id')     /*single element, unique*/
$('.class')     /*list of all class, same as CSS selector*/
$('li')     /*return list of ALL li*/
/*
[jQ CDN]
https://developers.google.com/speed/libraries/#jquery
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
[jQ]
$ === jQuery returns "function (a,b){return new n.fn.init(a,b)}"
*/
