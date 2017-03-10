// Copyright LostGods

#pragma once

#include "GameFramework/Actor.h"
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

protected:
	UPROPERTY(EditDefaultsOnly)
		uint32 bCanInteract : 1;

	UPROPERTY(EditDefaultsOnly)
		uint32 bTouchInteracts : 1;

	//UPROPERTY(EditDefaultsOnly)
		//EStencilColor StencilColor;

private:
	UStaticMeshComponent* StaticMesh;
	TArray<UMeshComponent*> Meshes;
};