<script lang="ts">
	import type { QuestionQueueEntry } from "$lib/game";

	export let questions: Array<QuestionQueueEntry> = [];
</script>

<table class="table is-fullwidth is-hoverable is-striped">
	<tbody>
		{#each questions as question, i}
			<tr>
				<td class="has-text-right">
					{i + 1}
				</td>
				<td class="has-text-right">
					{question.question.text}
				</td>
			</tr>
		{/each}
	</tbody>
</table>
