<script lang="ts">
	import { goto } from "$app/navigation";
	import { gameManagerStore } from "$lib/state";

	function returnToHome() {
		gameManagerStore.set(undefined);
		goto("/");
	}
</script>

<p class="has-text-centered">
	<button class="button is-link is-medium" on:click={returnToHome}>
		Play Again
	</button>
</p>
