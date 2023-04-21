<script lang="ts">
	import { goto } from "$app/navigation";
	import PageHeader from "$lib/PageHeader.svelte";
	import StdContainer from "$lib/StdContainer.svelte";
	import type { GameManager, QuestionUI } from "$lib/game";
	import { gameManagerStore } from "$lib/state";

	let gameManager: GameManager | undefined;
	let currentQuestion: QuestionUI;

	gameManagerStore.subscribe((value) => {
		gameManager = value;
	});

	if (!gameManager) {
		goto("/");
	}

	currentQuestion = gameManager!.getQuestion();

	$: qIndex = "Question " + (currentQuestion.qIndex + 1);
</script>

<PageHeader bind:text={qIndex} />

<StdContainer>
	{currentQuestion.question.text}
</StdContainer>
