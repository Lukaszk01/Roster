{% extends "main/base.html" %}
{% block content %}
<script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.2.3/velocity.min.js"></script>


<div id="example-3">
  <button v-on:click="say('hi')">Say hi</button>
  <button v-on:click="say('what')">Say what</button>
</div>

</script>
<style scoped>
  #staggered-list-demo {
    color: pink;

}
</style>
{% endblock %}