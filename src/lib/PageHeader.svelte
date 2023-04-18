<script lang="ts">
	import { appName } from "./const";
	export let text: String = appName;
	export let centerText: Boolean = true;
	export let color: String = "link";
</script>

<section class="hero is-small is-{color}">
	<div class="hero-body">
		<p class="title is-size-1 {centerText ? 'has-text-centered' : ''}">
			{text}
		</p>
	</div>
</section>
