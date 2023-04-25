<script lang="ts">
	import { QuestionState, type QuestionQueueEntry } from "$lib/game";

	export let questions: Array<QuestionQueueEntry> = [];
</script>

<div class="box">
	<table class="table is-fullwidth is-striped">
		<thead>
			<tr class="has-text-weight-semibold">
				<td>Number</td>
				<td>Question</td>
				<td>Your Answer</td>
			</tr>
		</thead>
		<tbody>
			{#each questions as question, i}
				<tr>
					<td class="has-text-right">
						{i + 1}
					</td>
					<td>
						{question.question.text}
					</td>
					<td class="has-text-left">
						{#if question.state == QuestionState.TRUE}
							&#129001; Correct!
						{:else}
							&#128997; Wrong :P
						{/if}
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
