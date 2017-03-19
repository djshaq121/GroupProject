// Copyright LostGods

#pragma once

#include "GameFramework/Actor.h"
#include "GroupProject.h"
#include "InteractableActor.generated.h"

UCLASS()
class GROUPPROJECT_API AInteractableActor : public AActor
{
	GENERATED_BODY()
	
public:
	AInteractableActor();

	UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category = "Interaction")
		void OnInteract(AActor* Caller);
	virtual void OnInteract_Implementation(AActor* Caller);

	void OnBeginFocus();
	void OnEndFocus();
	void SetCanInteract(bool newCanInteract);

	UFUNCTION()
		void OnOverlapBegin(AActor* OtherActor, AActor* thisActor);

	virtual void BeginPlay() override;
	virtual void Tick(float DeltaSeconds) override;

	//This is the name of the Interactable actor to be displayed on screen - e.g. Shop
	UPROPERTY(EditDefaultsOnly)
	FString Name;
	//This is the action that we describe when the player interacts with this actor -e.g. Open Shop
	UPROPERTY(EditDefaultsOnly)
	FString Action;
	//This returns a string which id displayed to the screen when the user looks at an Interactable actor
	UFUNCTION(BlueprintCallable,Category = "Interaction")
	FString GetUseText() const { return FString::Printf(TEXT("%s : Press E to %s"), *Name, *Action); }

protected:
	UPROPERTY(EditDefaultsOnly)
		uint32 bCanInteract : 1;

	UPROPERTY(EditDefaultsOnly)
		uint32 bTouchInteracts : 1;

	UPROPERTY(EditDefaultsOnly)
	EStencilColor StencilColor;

private:
	UStaticMeshComponent* StaticMesh;
	TArray<UMeshComponent*> Meshes;
};