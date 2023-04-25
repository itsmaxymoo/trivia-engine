<script lang="ts">
	import { goto } from "$app/navigation";
	import PageHeader from "$lib/PageHeader.svelte";
	import StdContainer from "$lib/StdContainer.svelte";
	import type { GameManager } from "$lib/game";
	import { gameManagerStore } from "$lib/state";
	import QuestionResults from "./QuestionResults.svelte";
	import ReturnButton from "./ReturnButton.svelte";

	let gameManager: GameManager | undefined;

	// --- Ensure the game is in a valid state
	gameManagerStore.subscribe((value) => {
		gameManager = value;
	});

	if (!gameManager) {
		goto("/");
	}

	let questions = gameManager!.questionArray;
</script>

<PageHeader text="Results" />

<StdContainer>
	<QuestionResults bind:questions />

	<ReturnButton />
</StdContainer>
