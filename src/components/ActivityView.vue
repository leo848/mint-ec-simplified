<script lang="ts">
import Vue from "vue";
import CreateActivityDialog from "./CreateActivityDialog.vue";

export default Vue.extend({
	name: "ActivityView",
	data: () => ({
		user: {},
	}),
	components: { CreateActivityDialog },
	created() {
		this.user = JSON.parse(sessionStorage.getItem("user") as string);
	},
});
</script>

<template>
	<div class="wrapper">
		<h1 class="text-h3 mt-4 mb-4">Deine Aktivitäten</h1>
		<v-row>
			<v-col
				cols="12"
				sm="6"
				v-for="activity in user.created_activities"
				:key="activity.id"
			>
				<v-card class="mx-auto">
					<v-card-title> {{ activity.title }} </v-card-title>
					<v-card-subtitle> {{ activity.description }} </v-card-subtitle>
					<v-card-actions>
						<v-tooltip bottom>
							<template v-slot:activator="{ on, attrs }">
								<v-btn
									icon
									v-if="activity.review_status === 0"
									v-bind="attrs"
									v-on="on"
								>
									<v-icon large>mdi-dots-horizontal-circle</v-icon>
								</v-btn>
								<v-btn
									icon
									v-else-if="activity.review_status === 1"
									v-bind="attrs"
									v-on="on"
								>
									<v-icon large color="green">mdi-check-circle</v-icon>
								</v-btn>
								<v-btn
									icon
									v-else-if="activity.review_status === -1"
									v-bind="attrs"
									v-on="on"
								>
									<v-icon large color="red">mdi-close-circle</v-icon>
								</v-btn>
							</template>
							<span>
								{{
									activity.review_status === 0
										? "Noch nicht bearbeitet"
										: activity.review_status === 1
										? "Bestätigt"
										: activity.review_status === -1
										? "Abgelehnt"
										: "Unbekannter Status"
								}}
							</span>
						</v-tooltip>
						<v-spacer />
						<v-btn icon>
							<v-icon>mdi-pencil</v-icon>
						</v-btn>
					</v-card-actions>
				</v-card>
			</v-col>
		</v-row>
		<CreateActivityDialog />
	</div>
</template>
