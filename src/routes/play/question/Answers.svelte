<script lang="ts">
	export let answers: Array<String> = [];
</script>

<div class="box has-text-centered">
	<table class="table is-fullwidth is-hoverable is-striped">
		<tbody>
			{#each answers as answer}
				<tr>
					<td class="has-text-left">{answer}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
