{% extends "main/base.html" %}
{% block content %}
<script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.2.3/velocity.min.js"></script>


<span>Multiline message is:</span>
<p style="white-space: pre-line;">{{ message }}</p>
<br>
<textarea v-model="message" placeholder="add multiple lines"></textarea>
</script>
<style scoped>
  #staggered-list-demo {
    color: pink;

}
</style>
{% endblock %}