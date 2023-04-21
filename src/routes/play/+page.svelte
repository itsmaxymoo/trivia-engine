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
</script>

<PageHeader text="Playing!" />

<StdContainer>
	{currentQuestion.question.text}
</StdContainer>
