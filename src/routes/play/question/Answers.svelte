<script lang="ts">
	export let answers: Array<String> = [];
</script>

<div class="box has-text-centered">
	{#each answers as answer}
		<button class="button is-medium is-info is-outlined">{answer}</button>
	{/each}
</div>
